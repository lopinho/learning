import { Test } from '@nestjs/testing';
import { assert } from 'console';
import { AuthService } from './auth.service';
import { User } from './users.entity';
import { UsersService } from './users.service';

describe('AuthService', () => {
  let service: AuthService;
  let fakeUsersService: Partial<UsersService>;

  beforeEach(async () => {
    fakeUsersService = {
      find: () => Promise.resolve([]),
      create: (email: string, password: string) =>
        Promise.resolve({ id: 1, email, password } as User),
    };
    const module = await Test.createTestingModule({
      providers: [
        AuthService,
        {
          provide: UsersService,
          useValue: fakeUsersService,
        },
      ],
    }).compile();
    service = module.get(AuthService);
  });

  it('can create an instance of auth service', async () => {
    expect(service).toBeDefined();
  });

  it('creates a new user with a salted and hashed password', async () => {
    const password = 'fooBar';
    const user = await service.signUp('test@example.com', password);
    expect(user.password).not.toEqual(password);
    const [salt, hash] = user.password.split('.');
    expect(salt).toBeDefined();
    expect(hash).toBeDefined();
  });

  it('throws an error if user signs up with email that is in use', (done) => {
    fakeUsersService.find = () =>
      Promise.resolve([{ id: 1, email: 'a', password: '1' } as User]);
    service.signUp('asdf@asdf.com', 'asdf').catch(() => done());
  });

  it('throws if signin is called with wrong email', (done) => {
    service.signIn('invalid@email.com', 'password').catch(() => done());
  });

  it('throws if invalid password is provided', (done) => {
    const email = 'user@email.com';
    fakeUsersService.find = () =>
      Promise.resolve([
        { id: 1, email: email, password: 'correctPassword' } as User,
      ]);
    service.signIn(email, 'wrongpassord').catch(() => done());
  });

  it('return user if correct password is provided', async () => {
    const email = 'user@email.com';
    fakeUsersService.find = () =>
      Promise.resolve([
        {
          id: 1,
          email: email,
          password:
            'd51a9e144a30c2de.5326cc8cd544bc7b43457b691269b2e3693c9ff79bda8cc2c91e789719cf00bc',
        } as User,
      ]);
    const user = await service.signIn(email, 'correctPassword');
    expect(user).toBeDefined();
  });
});
