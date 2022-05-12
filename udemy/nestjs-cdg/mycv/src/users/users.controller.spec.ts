import { Test, TestingModule } from '@nestjs/testing';
import { AuthService } from './auth.service';
import { UsersController } from './users.controller';
import { User } from './users.entity';
import { UsersService } from './users.service';

describe('UsersController', () => {
  let controller: UsersController;
  let fakeUserService: Partial<UsersService>;
  let fakeAuthService: Partial<AuthService>;

  beforeEach(async () => {
    fakeAuthService = {
      signIn: (email: string, password: string) => {
        return Promise.resolve({ id: 1, email, password } as User);
      },
      signUp: (email: string, password: string) => {
        return Promise.resolve({ id: 1, email, password } as User);
      },
    };
    fakeUserService = {
      findOne: (id: number) => {
        return Promise.resolve({
          id,
          email: 'teste@example.com',
          password: 'fooBar',
        } as User);
      },
      find: (email: string) => {
        return Promise.resolve([{ id: 1, email, password: 'fooBar' } as User]);
      },
      remove: (id: number) => {
        return Promise.resolve();
      },
      update: (id: number, attrs: Partial<User>) => {
        return Promise.resolve();
      },
    };

    const module: TestingModule = await Test.createTestingModule({
      controllers: [UsersController],
      providers: [
        { provide: UsersService, useValue: fakeUserService },
        { provide: AuthService, useValue: fakeAuthService },
      ],
    }).compile();

    controller = module.get<UsersController>(UsersController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });

  it('findallusers returns a list of users with the same email', async () => {
    const email = 'teste@example.com';
    const users = await controller.findAllUsers(email);
    expect(users.length).toBe(1);
    expect(users[0].email).toBe(email);
  });

  it('findUser shoould return the user with correct id', async () => {
    const user = await controller.findUser('1');
    expect(user).toBeDefined();
  });
});
